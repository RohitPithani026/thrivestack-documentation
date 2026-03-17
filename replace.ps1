$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    $pattern = '(?s)<div class="toc-promo glass-panel">\s*<div class="promo-icon"><i class="fa-solid fa-rocket gradient-text"></i></div>\s*<h5>Ready to scale\?</h5>\s*<p>Book a demo with our growth team today\.</p>.*?</div>'
    $replacement = '<ready-to-scale-promo></ready-to-scale-promo>'
    
    # We want to keep the indentation if possible, but let's just replace the whole tag directly.
    $newContent = [regex]::Replace($content, $pattern, $replacement)
    
    if ($content -cne $newContent) {
        Write-Host "Replaced in $($file.Name)"
        # Use UTF8 without BOM
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($file.FullName, $newContent, $utf8NoBom)
    }
}
