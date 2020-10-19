
run:
	$(info Input should be encode/decode, plaintext, key)

	encode: cipher.py
	py cipher.py $(ARGS)
