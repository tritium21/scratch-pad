# https://www.reddit.com/r/PowerShell/comments/21jzf1/du_hsc_from_bash_for_powershell/cge3gwz/
# du . | sort -Descending Size

Function Get-DU
{   Param (
        $Path = "."
    )
    ForEach ($File in (Get-ChildItem $Path))
    {   If ($File.PSisContainer)
        {   $Size = [Math]::Round((Get-ChildItem $File.FullName -Recurse | Measure-Object -Property Length -Sum).Sum / 1KB,2)
            $Type = "Folder"
        }
        Else
        {   $Size = $File.Length
            $Type = ""
        }
        [PSCustomObject]@{
            Name = $File.Name
            Type = $Type
            Size = $Size
        }
    }
}
Set-Alias -Name du -Value Get-DU
