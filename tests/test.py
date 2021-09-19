# Tests

import src.libautomate as libautomate


# print(libautomate.findImageAndClick("testimgs/tab.PNG"))

# idx = libautomate.findImgInListAndClick(
# [ "testimgs/tabGrey.PNG", "testimgs/tabLit.PNG"]
# )

lastFoundIdx = libautomate.zeroInByImgSeqAndClick(
[ "testimgs/tab1Grey.PNG", "testimgs/tabCloseBtn.PNG"]
)

print(lastFoundIdx)
