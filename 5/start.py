# import fun7
import pakiet  # import pakietu
from pakiet import fun  # import pliku z pakietu
import pakiet.fun as pk  # import pliku z pakietu

# fun7.all_params()
fun.powitanie()  # Cześć
pk.powitanie()  # Cześć

# Po dodaniu __all__ = ['info'] w pliku __init__.py
pakiet.info()  # Jestem pakietem
