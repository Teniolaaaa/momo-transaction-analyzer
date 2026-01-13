git filter-branch -f --msg-filter '
    if ($_ -match "Add CSS styling") { "added dashboard styling" }
    elseif ($_ -match "Project implementation") { "initial commit with all files" }
    elseif ($_ -match "Add project documentation") { "added docs" }
    elseif ($_ -match "Update architecture docs") { "updated architecture file" }
    elseif ($_ -match "Update scrum board") { "scrum board update" }
    elseif ($_ -match "Fix CSS and JS file paths") { "fixed file paths" }
    elseif ($_ -match "Move CSS and JS to root") { "moved css and js files" }
    elseif ($_ -match "Update transaction dates") { "update dates" }
    elseif ($_ -match "Update data files with new dates") { "added new transaction data" }
    elseif ($_ -match "Update dashboard with recent dates") { "dashboard update with recent dates" }
    elseif ($_ -match "Add architecture diagram") { "added system diagram" }
    elseif ($_ -match "Update README") { "readme changes" }
    elseif ($_ -match "Simplify project management") { "simplified docs" }
    elseif ($_ -match "add known issues") { "added team info and issues" }
    elseif ($_ -match "clean up readme") { "cleaned up readme" }
    else { $_ }
' HEAD~15..HEAD
