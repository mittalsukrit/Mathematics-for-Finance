Get-ChildItem -Filter "*.md" | ForEach-Object {
    $mdfile = $_.Name
    $htmlfile = $_.BaseName + ".html"
    pandoc $mdfile -f gfm -s --mathjax -c https://cdnjs.cloudflar.com/ajax/libs/github-markdown-css/5.5.1/github-markdown.min.css -c wide.css -o $htmlfile
}