BEGIN {start = 1; chinese = ""; english = ""}
/^[0-9]+\. / {
    if (start == 0) printf "%s\t%s\n", chinese, english
    start = 1
    english = ""
    # 提取中文并存储
    sub(/^[0-9]+\. /, "")
    chinese = $0
    next
}
/^ +- / {
    # 处理英文行
    start = 0
    if (english != "") english=english "<br>"
    sub(/^ +- /,"")
    english=english $0
}
END {if (start == 0) printf "%s\t%s\n", chinese, english}