from enum import Enum

class cell(Enum):
	DR = 0x250F # Down + Right
	DL = 0x2513 # Down + Left
	UR = 0x2517 # Up + Right
	UL = 0x252B # Up + Left
	VR = 0x2523 # Vertical + Right
	VL = 0x252B # Vertical + Left
	HD = 0x2533 # Horizonal + Down
	HU = 0x253B # Horizonal + Up
	HO = 0x2501 # Horizonal
	VE = 0x2503 # Vertical
	HV = 0x254B # Horizonal + Vertical
	BL = 0x25A0 # Block