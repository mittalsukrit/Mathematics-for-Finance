Get-ChildItem -Filter "*.md" | ForEach-Object {
    $mdfile = $_.Name
    $htmlfile = $_.BaseName + ".html"
    pandoc $mdfile -f markdown+raw_html -s --mathjax -c lecture-theme.css --metadata title="$($_.BaseName)" -o $htmlfile
}