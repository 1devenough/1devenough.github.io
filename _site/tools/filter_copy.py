#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파일 필터 복사 스크립트 (filter_copy.py)

지정된 원본 폴더(들)에서 대상 폴더로 파일을 복사한다.
'include' 및 'exclude' 문자열 목록을 기반으로 파일을 필터링한다.

[필터링 규칙]
1. Exclude 우선: 파일의 상대 경로가 'exclude' 목록의 문자열을 하나라도 포함하면,
   'include' 목록에 있어도 무조건 제외된다.
2. Include (선택적):
   - 'include' 목록이 비어 있으면: Exclude되지 않은 모든 파일이 복사된다.
   - 'include' 목록이 있으면: Exclude되지 않은 파일 중, 상대 경로가 'include'
     목록의 문자열을 하나라도 포함해야만 복사된다.

[사용 예시]
# 'src' 폴더의 .py, .md 파일만 'backup' 폴더로 복사 (단, 'tests' 폴더는 제외)
python filter_copy.py src backup --include .py .md --exclude tests/

# 여러 소스 폴더('src1', 'src2')를 'dest'로 병합 (단, .log 파일과 __pycache__ 제외)
python filter_copy.py src1 src2 dest --exclude .log __pycache__ -v
"""

import shutil
import sys
import argparse
from pathlib import Path
from typing import List

def _is_file_allowed(path_str: str, includes: List[str], excludes: List[str]) -> bool:
    """
    논의된 필터링 로직을 적용하여 파일 복사 여부를 결정한다.

    :param path_str: 슬래시(/)로 정규화된 파일의 상대 경로 문자열
    :param includes: 포함 규칙 문자열 리스트
    :param excludes: 제외 규칙 문자열 리스트
    :return: 복사 여부 (True/False)
    """

    # 1. Exclude 규칙이 항상 우선
    for pattern in excludes:
        if pattern in path_str:
            # 제외 규칙에 하나라도 걸리면 즉시 False 반환
            return False

    # 2. Include 규칙 검사 (Exclude에 걸리지 않은 파일 대상)
    if not includes:
        # Include 목록이 비어있으면 (규칙 없음) -> 통과
        return True

    # Include 목록이 지정된 경우, 하나라도 일치해야 함
    for pattern in includes:
        if pattern in path_str:
            # 포함 규칙에 하나라도 걸리면 -> 통과
            return True

    # Include 목록이 있으나, 위에서 하나도 일치하지 않음 -> 제외
    return False

def copy_files(
    source_dirs: List[Path],
    dest_dir: Path,
    includes: List[str],
    excludes: List[str],
    verbose: bool = False
):
    """
    정의된 규칙에 따라 하나 이상의 원본 폴더에서 대상 폴더로 파일을 복사한다.

    :param source_dirs: 원본 폴더 경로 객체 리스트
    :param dest_dir: 대상 폴더 경로 객체
    :param includes: 포함 규칙 문자열 리스트
    :param excludes: 제외 규칙 문자열 리스트
    :param verbose: 자세한 로그 출력 여부
    """

    print(f"🎯 대상 폴더: {dest_dir.resolve()}")
    print(f"🟢 포함 규칙: {includes if includes else '[모든 파일]'}")
    print(f"🔴 제외 규칙: {excludes if excludes else '[없음]'}")
    print("-" * 30)

    copied_count = 0

    # 대상 폴더가 없으면 생성
    dest_dir.mkdir(parents=True, exist_ok=True)

    for source_dir in source_dirs:
        # 원본 폴더 경로를 절대 경로로 변환하여 사용
        abs_source_dir = source_dir.resolve()

        if not abs_source_dir.is_dir():
            print(f"⚠️ 경고: 원본 폴더 '{abs_source_dir}'를 찾을 수 없습니다. 건너뜁니다.", file=sys.stderr)
            continue

        print(f"🔍 '{abs_source_dir}' 폴더를 스캔 중...")

        # rglob('*')로 모든 하위 파일/폴더 순회
        for item_path in abs_source_dir.rglob('*'):
            if item_path.is_file():
                # 원본 폴더 기준 상대 경로 계산
                try:
                    relative_path = item_path.relative_to(abs_source_dir)
                except ValueError:
                    # 심볼릭 링크 또는 경로 계산이 어려운 경우 예외 처리
                    print(f"⚠️ 상대 경로 계산 실패: {item_path}. 건너뜁니다.", file=sys.stderr)
                    continue

                # POSIX 스타일 경로 문자열로 변환 (일관된 비교를 위해 '/')
                relative_path_str = relative_path.as_posix()

                # 필터링 로직 적용
                if _is_file_allowed(relative_path_str, includes, excludes):
                    # 대상 파일 경로 계산 (원본의 상대 경로를 그대로 유지)
                    destination_path = dest_dir / relative_path

                    # 대상 폴더 생성 (필요한 경우)
                    destination_path.parent.mkdir(parents=True, exist_ok=True)

                    try:
                        # 파일 복사 (메타데이터 포함)
                        shutil.copy2(item_path, destination_path)
                        if verbose:
                            print(f"  [복사] {relative_path_str}")
                        copied_count += 1
                    except Exception as e:
                        print(f"❌ 복사 오류 '{item_path}': {e}", file=sys.stderr)

    print("-" * 30)
    print(f"🎉 총 {copied_count}개의 파일 복사 완료.")

def main():
    """
    명령줄 인자를 파싱하여 copy_files 함수를 실행한다.
    """
    parser = argparse.ArgumentParser(
        description="지정된 규칙(include/exclude 문자열)에 따라 파일을 복사한다.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
[규칙 설명]
  -x, --exclude: 하나라도 포함되면 무조건 제외 (가장 높은 우선순위)
  -i, --include: 이 목록이 비어있으면 '모두'를 의미함.
                 하나라도 지정되면, exclude에 걸리지 않은 파일 중
                 이 목록의 문자열 중 하나를 포함해야만 복사됨.

[예시]
  python %(prog)s ./src ./backup -i .py .md -x tests/ __pycache__
  (src 폴더에서 tests와 __pycache__를 제외한 .py와 .md 파일만 backup로 복사)
"""
    )

    parser.add_argument(
        "source_dirs",
        metavar="SOURCE_DIR",
        type=Path,
        nargs='+',
        help="복사할 원본 폴더 (하나 이상 지정 가능)"
    )
    parser.add_argument(
        "dest_dir",
        metavar="DEST_DIR",
        type=Path,
        help="파일이 복사될 대상 폴더"
    )
    parser.add_argument(
        "-i", "--include",
        nargs='*',  # 0개 이상
        default=[],
        help="상대 경로에 포함되어야 하는 문자열 목록. (기본값: 모두)"
    )
    parser.add_argument(
        "-x", "--exclude",
        nargs='*',  # 0개 이상
        default=[],
        help="상대 경로에 포함될 경우 제외하는 문자열 목록. (Include보다 우선)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="자세한 파일 복사 로그를 출력합니다."
    )

    args = parser.parse_args()

    try:
        copy_files(args.source_dirs, args.dest_dir, args.include, args.exclude, args.verbose)
    except KeyboardInterrupt:
        print("\n작업이 사용자에 의해 중단되었습니다.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n심각한 오류 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
