# Spell to make plots appear in PyCharm

```matplotlib.use('TkAgg')```

Usage:

```
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

matplotlib.use('TkAgg')
img = Image.open('C:\\Temp\\test.png')
plt.figure()
imgplot = plt.imshow(img)
plt.show()
```
