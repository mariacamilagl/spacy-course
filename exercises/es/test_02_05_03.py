def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "¿Estás importando la clase Doc correctamente?"
    assert len(words) == 5, "Parece que tienes el número incorrecto de palabras."
    assert len(spaces) == 5, "Parece que tienes el número incorrecto de espacios."
    assert words == ["Oh", ",", "really", "?", "!"], "¡Chequea otra vez las palabras!"
    assert all(isinstance(s, bool) for s in spaces), "Los espacios tienen que ser booleanos."
    assert [int(s) for s in spaces] == [0, 1, 0, 0, 0], "¿Están los espacios correctos?"
    assert doc.text == "Oh, really?!", "¿Creaste el Doc correctamente?"
    __msg__.good("¡Buen trabajo! A continuación, creemos algunas entidades.")
