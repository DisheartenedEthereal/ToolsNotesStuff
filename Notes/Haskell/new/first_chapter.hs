doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100
			 then x
			 else doubleMe x
doubleSmallNumber' x = (if x > 100 then x else doubleMe x)

conanO'Brien = "Hello, i love this language"
