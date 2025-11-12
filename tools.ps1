function Code-Backup {
    # 예: 현재 폴더(.)를 ../backup/my_project로 복사
    # 단, .py, .md, Gemfile, Dockerfile만 포함
    # 그리고 node_modules, .git, .idea 폴더는 제외

    $sources = "."
    $destination = "../../backup/my_project_$(Get-Date -Format yyyy_MM_dd_HH_MM_ss_fff)"

    $includes = @(
        ".py",
        ".md",
        "Gemfile",
        ".html",
        ".css",
        ".scss",
        ".yml",
        ".ps1"
    )

    $excludes = @(
        ".git/",
        ".idea/",
        "_site/",
        ".jekyll-cache/",
        "__pycache__",
        "Gemfile.lock",
        "concat_to_md.py",
        "filter_copy.py",
        ".ps1"
    )

    # Python 스크립트 실행
    python ./tools/filter_copy.py $sources $destination --include $includes --exclude $excludes --verbose
}

function Code-Concat-To_MD {
    # 예: 현재 폴더(.)를 ../backup/my_project로 복사
    # 단, .py, .md, Gemfile, Dockerfile만 포함
    # 그리고 node_modules, .git, .idea 폴더는 제외

    $sources = "."
    $destination = "../../backup/my_project_$(Get-Date -Format yyyy_MM_dd_HH_MM_ss_fff).md"

    $includes = @(
        ".py",
        ".md",
        "Gemfile",
        ".html",
        ".css",
        ".scss",
        ".yml"
    )

    $excludes = @(
        ".git/",
        ".idea/",
        "_site/",
        ".jekyll-cache/",
        "__pycache__",
        "Gemfile.lock",
        "concat_to_md.py",
        "filter_copy.py",
        ".ps1"
    )

    # Python 스크립트 실행
    python ./tools/concat_to_md.py $sources $destination --include $includes --exclude $excludes --verbose
}

