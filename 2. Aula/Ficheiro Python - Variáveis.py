# %% [markdown]
# # 1. Variáveis
# 
# ## 1.1. Atribuição direta

# %%
x = 10 # Atribuição direta de um numero inteiro
y = 4.7 # Atribuição direta de um numero float
s = 'Python' # Atribuição direta de um caracter ou conjunto de caracteres
t = "Python" # Atribuição direta de um caracter ou conjunto de caracteres
r = '4' # Diferente de inteiro. 4 é uma string
w = "'3'" # Colocação de aplica em string
v = '"3"' # Colocação de aspas em string

# %%
X = 20

# %%
# y + r

# %% [markdown]
# ## 1.2. Atribuição por Construtor ou *Casting*

# %%
x1 = int(y) # Converter float para inteiro
x2 = float(x) # Converter inteiro para float

x3 = int(r) # Converter string para inteiro. Operação válida se a string apenas conttiver numeros

# x4 = int(s) # Operação inválida, uma vez que a string contém caracteres

x5 = float(r) # Converter string para float
x6 = 16514861156561615313165

x7 = str(x6)

'olá eu sou o João' + 'O seu apelido é Araújo'

# %%
y + x3

# %%
y + x6

# %%
r + x7

# %% [markdown]
# ## 1.3. Case-sensitive

# %%
a = 'João' #a diferente de A
A = 'João'

# %% [markdown]
# ## 1.4. Tipos de variável

# %%
print(type(y))


