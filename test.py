# Copyright (C) 2021 - Abhijit Nandy

# Tests
import libautomate


# print(libautomate.findImageAndClick("testimgs/tab.PNG"))

# lastFoundIdx = libautomate.findImgInListAndClick(
# [ "testimgs/tabGrey.PNG", "testimgs/tabLit.PNG"]
# )

# lastFoundIdx = libautomate.zeroInByImgSeqAndClick(
# [ "testimgs/tab1Grey.PNG", "testimgs/tabCloseBtn.PNG"]
# )



lastFoundIdx = libautomate.findImgInListClickType(
    [ "testimgs/folderPathBar.PNG"], "Hello"
)
print(lastFoundIdx)
