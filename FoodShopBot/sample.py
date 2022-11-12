from PIL import Image
#
#
# def main():
#     try:
#         Image.open("pepsi.jpg")
#
#     except IOError:
#         pass
#
#
# if __name__ == "__main__":
#     main()
try:
    img = Image.open("pepsi.jpg")
except IOError:
    pass
