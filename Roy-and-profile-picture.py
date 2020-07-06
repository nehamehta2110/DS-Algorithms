"""Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.
Minimum dimension of the picture can be L x L, where L is the length of the side of square.
Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H
where W - width of the photo and H - Height of the photo
#When any photo is uploaded following events may occur:
[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
(b) else user is prompted to crop it. Print "CROP IT" in this case."""


def isPhotoAccepted(L, W, H):

    if W < L or H < L:
        result = 'UPLOAD ANOTHER'
        print('%s' % result)

    elif W != H:
        result = 'CROP IT'
        print('%s' % result)

    else:
        result = 'ACCEPTED'
        print('%s' % result)


def main():
    L = int(input())
    N = int(input())

    for i in range(N):
        a = list(map(int, input().split()))
        W = a[0]
        H = a[1]
        isPhotoAccepted(L, W, H)

