from catalog_a import PRODUCTS_A
from catalog_b import PRODUCTS_B, BUNDLE
PRODUCTS = PRODUCTS_A + PRODUCTS_B
ALL = PRODUCTS + [BUNDLE]

# the eight product files that go inside the bundle ZIP
BUNDLE_FILES = [p["files"][0] for p in PRODUCTS]
