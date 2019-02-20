TB = "    /"
End = "    \n"
Centre1 = "  1 /"
Centre2 = "  2 /"
Centre3 = "  3 \n"
Centre4 = "  4 /"
Centre5 = "  5 /"
Centre6 = "  6 \n"
Centre7 = "  7 /"
Centre8 = "  8 /"
Centre9 = "  9 \n"
Divide = "--------------\n"

# X replacement Strings
XTB = "X  X/"
XEnd = "X  X\n"
XCen = " XX /"
XEndCen = " XX \n"

# O replacement Strings
OTB = " OO /"
OEnd = " OO \n"
OCen = "O  O/"
OEndCen = "O  O\n"

Line1 = TB + TB + End
Line2 = Centre1 + Centre2 + Centre3
Line3 = TB + TB + End
Line4 = TB + TB + End
Line5 = Centre4 + Centre5 + Centre6
Line6 = TB + TB + End
Line7 = TB + TB + End
Line8 = Centre7 + Centre8 + Centre9
Line9 = TB + TB + End

Player1Occupied = ()
Player2Occupied = ()
Player1Counter = ()
Player2Counter = ()

def p1check():
    while ["1"] in Player1Occupied:
        if Player1Counter == "X":
            Line1 = XTB + TB + End
            Line2 = XCen + Centre2 + Centre3
            Line3 = XTB + TB + End
        if Player1Counter == "O":
            Line1 = OTB + TB + End
            Line2 = OCen + Centre2 + Centre3
            Line3 = OTB + TB + End

    while "2" in Player1Occupied:
        if Player1Counter == "X":
            Line1 = TB + XTB + End
            Line2 = Centre1 + XCen + Centre3
            Line3 = TB + XTB + End
        if Player1Counter == "O":
            Line1 = TB + OTB + End
            Line2 = Centre1 + OCen + Centre3
            Line3 = TB + OTB + End

    while "3" in Player1Occupied:
        if Player1Counter == "X":
            Line1 = TB + TB + XEnd
            Line2 = Centre1 + Centre2 + XEndCen
            Line3 = TB + TB + XEnd
        if Player1Counter == "O":
            Line1 = TB + TB + OEnd
            Line2 = Centre1 + Centre2 + OEndCen
            Line3 = TB + TB + OEnd


    while "4" in Player1Occupied:
        if Player1Counter == "X":
            Line4 = XTB + TB + End
            Line5 = XCen + Centre5 + Centre6
            Line6 = XTB + TB + End
        if Player1Counter == "O":
            Line4 = OTB + TB + End
            Line5 = OCen + Centre5 + Centre6
            Line6 = OTB + TB + End

    while "5" in Player1Occupied:
        if Player1Counter == "X":
            Line4 = TB + XTB + End
            Line5 = Centre4 + XCen + Centre6
            Line6 = TB + XTB + End
        if Player1Counter == "O":
            Line4 = TB + OTB + End
            Line5 = Centre4 + OCen + Centre6
            Line6 = TB + OTB + End

    while "6" in Player1Occupied:
        if Player1Counter == "X":
            Line4 = TB + TB + XEnd
            Line5 = Centre4 + Centre5 + XEndCen
            Line6 = TB + TB + XEnd
        if Player1Counter == "O":
            Line4 = TB + TB + OEnd
            Line5 = Centre4 + Centre5 + OEndCen
            Line6 = TB + TB + OEnd


    while "7" in Player1Occupied:
        if Player1Counter == "X":
            Line7 = XTB + TB + End
            Line8 = XCen + Centre8 + Centre9
            Line9 = XTB + TB + End
        if Player1Counter == "O":
            Line7 = OTB + TB + End
            Line8 = OCen + Centre8 + Centre9
            Line9 = OTB + TB + End

    while "8" in Player1Occupied:
        if Player1Counter == "X":
            Line7 = TB + XTB + End
            Line8 = Centre7 + XCen + Centre9
            Line9 = TB + XTB + End
        if Player1Counter == "O":
            Line7 = TB + OTB + End
            Line8 = Centre7 + OCen + Centre9
            Line9 = TB + OTB + End

    while "9" in Player1Occupied:
        if Player1Counter == "X":
            Line7 = TB + TB + XEnd
            Line8 = Centre7 + Centre8 + XEndCen
            Line9 = TB + TB + XEnd
        if Player1Counter == "O":
            Line7 = TB + TB + OEnd
            Line8 = Centre7 + Centre8 + OEndCen
            Line9 = TB + TB + OEnd

    return 1


def p2check():
    while "1" in Player2Occupied:
        if Player2Counter == "X":
            Line1 = XTB + TB + End
            Line2 = XCen + Centre2 + Centre3
            Line3 = XTB + TB + End
        if Player2Counter == "O":
            Line1 = OTB + TB + End
            Line2 = OCen + Centre2 + Centre3
            Line3 = OTB + TB + End

    while "2" in Player2Occupied:
        if Player2Counter == "X":
            Line1 = TB + XTB + End
            Line2 = Centre1 + XCen + Centre3
            Line3 = TB + XTB + End
        if Player2Counter == "O":
            Line1 = TB + OTB + End
            Line2 = Centre1 + OCen + Centre3
            Line3 = TB + OTB + End

    while "3" in Player2Occupied:
        if Player2Counter == "X":
            Line1 = TB + TB + XEnd
            Line2 = Centre1 + Centre2 + XEndCen
            Line3 = TB + TB + XEnd
        if Player2Counter == "O":
            Line1 = TB + TB + OEnd
            Line2 = Centre1 + Centre2 + OEndCen
            Line3 = TB + TB + OEnd


    while "4" in Player2Occupied:
        if Player2Counter == "X":
            Line4 = XTB + TB + End
            Line5 = XCen + Centre5 + Centre6
            Line6 = XTB + TB + End
        if Player2Counter == "O":
            Line4 = OTB + TB + End
            Line5 = OCen + Centre5 + Centre6
            Line6 = OTB + TB + End

    while "5" in Player2Occupied:
        if Player2Counter == "X":
            Line4 = TB + XTB + End
            Line5 = Centre4 + XCen + Centre6
            Line6 = TB + XTB + End
        if Player2Counter == "O":
            Line4 = TB + OTB + End
            Line5 = Centre4 + OCen + Centre6
            Line6 = TB + OTB + End

    while "6" in Player2Occupied:
        if Player2Counter == "X":
            Line4 = TB + TB + XEnd
            Line5 = Centre4 + Centre5 + XEndCen
            Line6 = TB + TB + XEnd
        if Player2Counter == "O":
            Line4 = TB + TB + OEnd
            Line5 = Centre4 + Centre5 + OEndCen
            Line6 = TB + TB + OEnd


    while "7" in Player2Occupied:
        if Player2Counter == "X":
            Line7 = XTB + TB + End
            Line8 = XCen + Centre8 + Centre9
            Line9 = XTB + TB + End
        if Player2Counter == "O":
            Line7 = OTB + TB + End
            Line8 = OCen + Centre8 + Centre9
            Line9 = OTB + TB + End

    while "8" in Player2Occupied:
        if Player2Counter == "X":
            Line7 = TB + XTB + End
            Line8 = Centre7 + XCen + Centre9
            Line9 = TB + XTB + End
        if Player2Counter == "O":
            Line7 = TB + OTB + End
            Line8 = Centre7 + OCen + Centre9
            Line9 = TB + OTB + End

    while "9" in Player2Occupied:
        if Player2Counter == "X":
            Line7 = TB + TB + XEnd
            Line8 = Centre7 + Centre8 + XEndCen
            Line9 = TB + TB + XEnd
        if Player2Counter == "O":
            Line7 = TB + TB + OEnd
            Line8 = Centre7 + Centre8 + OEndCen
            Line9 = TB + TB + OEnd
    return 2