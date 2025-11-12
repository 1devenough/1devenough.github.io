#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파일 병합 스크립트 (concat_to_md.py)

지정된 원본 폴더(들)에서 파일들을 찾아 하나의 .md 파일로 병합한다.
'include' 및 'exclude' 문자열 목록을 기반으로 파일을 필터링한다.

[필터링 규칙]
1. Exclude 우선: 파일의 상대 경로가 'exclude' 목록의 문자열을 하나라도 포함하면,
   'include' 목록에 있어도 무조건 제외된다.
2. Include (선택적):
   - 'include' 목록이 비어 있으면: Exclude되지 않은 모든 파일이 병합된다.
   - 'include' 목록이 있으면: Exclude되지 않은 파일 중, 상대 경로가 'include'
     목록의 문자열을 하나라도 포함해야만 병합된다.

[출력 형식]
[relative/path/to/file.py]

```python
file_content_here
```

[사용 예시]
# 'src' 폴더의 .py, .md 파일만 'context.md'로 병합 (단, 'tests' 폴더는 제외)
python concat_to_md.py src context.md --include .py .md --exclude tests/

# 여러 소스 폴더('src', 'docs')를 'project.md'로 병합 (단, .log, __pycache__ 제외)
python concat_to_md.py src docs project.md --exclude .log __pycache__ -v
"""

import sys
import argparse
from pathlib import Path
from typing import List

# =============================================================================
# 유틸리티 함수
# =============================================================================

def _is_file_allowed(path_str: str, includes: List[str], excludes: List[str]) -> bool:
    """
    논의된 필터링 로직을 적용하여 파일 병합 여부를 결정한다.
    (filter_copy.py와 동일한 로직)
    """

    # 1. Exclude 규칙이 항상 우선
    for pattern in excludes:
        if pattern in path_str:
            return False

    # 2. Include 규칙 검사 (Exclude에 걸리지 않은 파일 대상)
    if not includes:
        return True

    for pattern in includes:
        if pattern in path_str:
            return True

    return False

def _get_md_lang(file_path: Path) -> str:
    """
    파일 경로(이름, 확장자)를 기반으로 마크다운 코드 블록 언어 태그를 반환한다.
    """
    name_lower = file_path.name.lower()

    # 확장자 없는 파일 특별 처리
    if name_lower == "gemfile":
        return "ruby"
    if name_lower == "dockerfile":
        return "dockerfile"
    if name_lower == "makefile":
        return "makefile"

    # 확장자 기반 매핑
    ext_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".kt": "kotlin",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".cs": "csharp",
        ".go": "go",
        ".rb": "ruby",
        ".php": "php",
        ".swift": "swift",
        ".rs": "rust",
        ".md": "markdown",
        ".json": "json",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".html": "html",
        ".css": "css",
        ".sh": "bash",
        ".ps1": "powershell",
        ".sql": "sql",
    }

    return ext_map.get(file_path.suffix.lower(), "text") # 모르면 'text'

# =============================================================================
# 메인 함수
# =============================================================================

def concat_to_markdown(
    source_dirs: List[Path],
    output_file: Path,
    includes: List[str],
    excludes: List[str],
    verbose: bool = False
):
    """
    정의된 규칙에 따라 하나 이상의 원본 폴더에서 파일 내용을 .md 파일로 병합한다.

    :param source_dirs: 원본 폴더 경로 객체 리스트
    :param output_file: 병합된 내용이 저장될 .md 파일 경로
    :param includes: 포함 규칙 문자열 리스트
    :param excludes: 제외 규칙 문자열 리스트
    :param verbose: 자세한 로그 출력 여부
    """

    print(f"🎯 대상 파일: {output_file.resolve()}")
    print(f"🟢 포함 규칙: {includes if includes else '[모든 파일]'}")
    print(f"🔴 제외 규칙: {excludes if excludes else '[없음]'}")
    print("-" * 30)

    merged_count = 0

    # 대상 파일의 상위 폴더가 없으면 생성
    output_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        # .md 파일을 쓰기 모드('w')로 열어 파일 내용을 초기화
        with open(output_file, 'w', encoding='utf-8') as f_out:

            for source_dir in source_dirs:
                abs_source_dir = source_dir.resolve()

                if not abs_source_dir.is_dir():
                    print(f"⚠️ 경고: 원본 폴더 '{abs_source_dir}'를 찾을 수 없습니다. 건너뜁니다.", file=sys.stderr)
                    continue

                print(f"🔍 '{abs_source_dir}' 폴더를 스캔 중...")

                # 정렬된 파일 목록을 얻기 위해 리스트로 변환
                all_files = sorted(list(abs_source_dir.rglob('*')))

                for item_path in all_files:
                    if item_path.is_file():
                        try:
                            relative_path = item_path.relative_to(abs_source_dir)
                        except ValueError:
                            print(f"⚠️ 상대 경로 계산 실패: {item_path}. 건너뜁니다.", file=sys.stderr)
                            continue

                        relative_path_str = relative_path.as_posix()

                        # 필터링 로직 적용
                        if _is_file_allowed(relative_path_str, includes, excludes):
                            try:
                                # 파일 내용 읽기
                                content = item_path.read_text(encoding='utf-8')
                                lang = _get_md_lang(item_path)

                                # 마크다운 블록 생성
                                output_block = f"\n\n[{relative_path_str}]\n\n```{lang}\n{content}\n```\n"

                                # .md 파일에 쓰기
                                f_out.write(output_block)

                                if verbose:
                                    print(f"  [병합] {relative_path_str}")
                                merged_count += 1

                            except UnicodeDecodeError:
                                if verbose:
                                    print(f"  [무시] {relative_path_str} (텍스트 파일 아님)")
                            except Exception as e:
                                print(f"❌ 읽기 오류 '{item_path}': {e}", file=sys.stderr)

    except IOError as e:
        print(f"❌ 파일 쓰기 오류 '{output_file}': {e}", file=sys.stderr)
        return
    except Exception as e:
        print(f"오류 발생: {e}", file=sys.stderr)
        return

    print("-" * 30)
    print(f"🎉 총 {merged_count}개의 파일을 '{output_file.name}' 파일로 병합 완료.")

def main():
    """
    명령줄 인자를 파싱하여 concat_to_markdown 함수를 실행한다.
    """
    parser = argparse.ArgumentParser(
        description="지정된 규칙(include/exclude 문자열)에 따라 파일 내용을 .md 파일로 병합한다.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
[규칙 설명]
  -x, --exclude: 하나라도 포함되면 무조건 제외 (가장 높은 우선순위)
  -i, --include: 이 목록이 비어있으면 '모두'를 의미함.
                 하나라도 지정되면, exclude에 걸리지 않은 파일 중
                 이 목록의 문자열 중 하나를 포함해야만 병합됨.

[예시]
  python %(prog)s ./src ./docs context.md -i .py .md Gemfile -x tests/
  (src, docs 폴더에서 tests를 제외한 .py, .md, Gemfile 파일만 context.md로 병합)
"""
    )

    parser.add_argument(
        "source_dirs",
        metavar="SOURCE_DIR",
        type=Path,
        nargs='+',
        help="검색할 원본 폴더 (하나 이상 지정 가능)"
    )
    parser.add_argument(
        "output_file",
        metavar="OUTPUT_FILE",
        type=Path,
        help="병합된 내용이 저장될 .md 파일 경로"
    )
    parser.add_argument(
        "-i", "--include",
        nargs='*',
        default=[],
        help="상대 경로에 포함되어야 하는 문자열 목록. (기본값: 모두)"
    )
    parser.add_argument(
        "-x", "--exclude",
        nargs='*',
        default=[],
        help="상대 경로에 포함될 경우 제외하는 문자열 목록. (Include보다 우선)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="자세한 파일 병합 로그를 출력한다."
    )

    args = parser.parse_args()

    try:
        concat_to_markdown(args.source_dirs, args.output_file, args.include, args.exclude, args.verbose)
    except KeyboardInterrupt:
        print("\n작업이 사용자에 의해 중단되었습니다.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n심각한 오류 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
