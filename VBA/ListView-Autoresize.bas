 ' A procedure to auto-resize column width of list view control
Sub AutoResizeListView(MyListView As Variant)
    ' Create a dynamic label and set it invisible
    Set MyLabel = Me.Controls.Add("Forms.Label.1", "Test Label", True)
    With MyLabel
        .Font.Size = MyListView.Font.Size
        .Font.Name = MyListView.Font.Name
        .WordWrap = False
        .AutoSize = True
        .Visible = False
    End With
    ' Auto-resize the first column
    MyLabel.Caption = MyListView.ColumnHeaders(1).Text
    MaxColumnWidth = MyLabel.Width
    For i = 1 To MyListView.ListItems.Count
        MyLabel.Caption = MyListView.ListItems(i).Text
        If MyLabel.Width > MaxColumnWidth Then
            MaxColumnWidth = MyLabel.Width
        End If
    Next i
    MyListView.ColumnHeaders(1).Width = MaxColumnWidth + 8
    ' Auto-resize the rest of columns
    For i = 1 To MyListView.ColumnHeaders.Count - 1
        MyLabel.Caption = MyListView.ColumnHeaders(i + 1).Text
        MaxColumnWidth = MyLabel.Width
        For j = 1 To MyListView.ListItems.Count
            MyLabel.Caption = MyListView.ListItems(j).SubItems(i)
            If MyLabel.Width > MaxColumnWidth Then
                MaxColumnWidth = MyLabel.Width
            End If
        Next j     'Next cell row in the current column
        MyListView.ColumnHeaders(i + 1).Width = MaxColumnWidth + 8
    Next i     'Next column
    Me.Controls.Remove MyLabel.Name    'Remove the dynamic label
End Sub

'Example with a list view and command button.
Private Sub CommandButton1_Click()
    CommandButton1.Caption = "Run"
    With ListView1
        .View = lvwReport
        .FullRowSelect = True
        .Gridlines = True
        With .ColumnHeaders
            .Clear
            .Add , , "Item", 70
            .Add , , "Subitem-1", 70
            .Add , , "Subitem-2", 70
        End With
        .ListItems.Clear
        With .ListItems.Add(, , "Main Item 1")
            .ListSubItems.Add , , "Subitem 1.1"
            .ListSubItems.Add , , "Subitem 1.2"
        End With
        With .ListItems.Add(, , "Main Item 2")
            .ListSubItems.Add , , "Subitem 2.1"
            .ListSubItems.Add , , "Subitem 2.2"
        End With
        With .ListItems.Add(, , "Main Item 3")
            .ListSubItems.Add , , "Subitem 3.1"
            .ListSubItems.Add , , "Subitem 3.2"
        End With
    End With
    Call AutoResizeListView(ListView1) 'note this call!
End Sub
