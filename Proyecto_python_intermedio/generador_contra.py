{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "039fb4d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A que plataforma corresponde: ubisoft\n",
      "A que Usuario corresponde la contraseña: legaka\n",
      "ubisoft: legaka; i68HpIs$DVoOywqP\n"
     ]
    }
   ],
   "source": [
    "from random import random, sample\n",
    "import random\n",
    "import pandas as pd \n",
    "\n",
    "lower = 'abcdefghijklmnñopqrstuvwxyz'\n",
    "upper = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'\n",
    "numero = '1234567890'\n",
    "simbol = '@#+*^<>}{][-_$%&/)(?!'\n",
    "dir_pandas = 'C:/Users/Usuario/proyecto1/Proyecto_python_intermedio/{}'.format('contraseñas.csv')\n",
    "\n",
    "all_ = lower + upper + numero + simbol\n",
    "length = 16\n",
    "\n",
    "\n",
    "password = \"\".join(random.sample(all_, length))\n",
    "\n",
    "plataforma =  input(\"A que plataforma corresponde: \")\n",
    "\n",
    "user = input(\"A que Usuario corresponde la contraseña: \")\n",
    "\n",
    "\n",
    "dict_pass = {\n",
    "    'Plataforma' :     [str(plataforma)],\n",
    "    'Usuario' : [str(user)],\n",
    "    'Contraseña' :    [str(password)]\n",
    "}\n",
    "\n",
    "cuenta = plataforma + \": \" + user + \"; \" + password\n",
    "\n",
    "df = pd.DataFrame(dict_pass)\n",
    "\n",
    "df.to_csv(dir_pandas, index = False)\n",
    "\n",
    "# with open('./contraseñas.csv', \"r+\", encoding=\"utf-8\") as f:\n",
    "#     f.write(df))\n",
    "\n",
    "\n",
    "print(cuenta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce1bcddc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
