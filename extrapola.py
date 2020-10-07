"""
  TOOLS IS BASED IN
  CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
  Copyright (C) 2020  

  DISCLAIMER: This file is for informational and educational purposes only. 
  We are not responsible for any misuse applied to it. All responsibility falls on the user

  ||================================================================================||
  || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
  ||================================================================================||

  Adapted BY lanniscaf ALL RIGHTS RESERVED
  """
class Extrapola:
  def __init__(self,bin1='',bin2=''):
    self.bin1=bin1
    self.bin2=bin2
    self.ccout=''

  #Extrapolacion por similitud
  def simpleE(self):
    self.ccout = ''
    if(len(self.bin1)!=16 or len(self.bin2)!=16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[:6] != self.bin2[:6]):
        return False
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == self.bin2[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
    else:
      self.ccout = False
    return self.ccout
  #Extrapolacion por lugar Banco
  def compleE(self):
    self.ccout = ''
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[:6] != self.bin2[:6]):
        return False
      cuerpo1 = self.bin1[:8]
      cuerpo2 = self.bin2[8:]
      #multiplica
      ccmult=''
      for num in range(len(cuerpo1)):
        ccmult = ccmult + str(int(cuerpo1[num])*int(cuerpo2[num]))
      #extragenerado
      cuerpo1+=ccmult[:8]
      #comparacion
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == cuerpo1[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
      if(self.ccout[15:]=='x'):
        self.ccout = self.ccout[:15]+'1'
      return(self.ccout)
  #Extrapolacion Avanzada
  def avanE(self):
    self.ccout = ''
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[6:8] != self.bin2[6:8]):
        return False
      elif(self.bin1[:6] != self.bin2[:6]):
        return False
      cuerpo1 = self.bin1[:8]
      mul1 = self.bin1[9:11]
      mul2 = self.bin2[9:11]
      #se suman
      mul1= str(int(mul1[0:1]) + int(mul1[1:]))
      mul2= str(int(mul2[0:1]) + int(mul2[1:]))
      #Re suman dobles
      while True:
        if(len(mul1) >= 2):
          mul1= str(int(mul1[0:1]) + int(mul1[1:]))
          continue
        elif(len(mul2) >= 2):
          mul2= str(int(mul2[0:1]) + int(mul2[1:]))
        else:
          break
      #Division
      mul1 = str(int(mul1) / 2)
      mul2 = str(int(mul2) / 2)
      #Multiplicacion
      mul1 = str(round(float(mul1)*5,))
      mul2 = str(round(float(mul2)*5,))
      #suma
      cuerpo1+=str(int(mul1)+int(mul2))
      self.ccout= cuerpo1
      for _ in range(6):
        self.ccout+='x'
      return(self.ccout)
        
    else:
      return False
  #Extrapolacion 343
  def grupE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout = self.bin1[:6]+self.bin1[6:7]+'x'+self.bin1[8:9]+self.bin1[9:10]+'xx'+self.bin1[12:13]+self.bin1[13:14]+'x'+self.bin1[15:]
      value=self.ccout
      return value
      

    else:
      return False
  #Extrapolacion 5
  def fivE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:11]
      for _ in range(5):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return False
  #Extrap X
  def xiE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:6]+'xxxx'+self.bin1[10:14]+'xx'
      return(self.ccout)
    else:
      return False
  #Extrapolacion X
  def xiiE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:10]
      for _ in range(6):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return False
  #Extrapolacion X
  def xiiiE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'x'+self.bin1[8:9]+'xxx'+self.bin1[12:14]+'xx'
      return(self.ccout)
    else:
      return False
  #Extrapolacion X
  def xiiiiE(self):
    if(not len(self.bin1)==16):
      return False
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'xx'+self.bin1[10:11]+'x'+self.bin1[12:13]+'xxxx'
      return(self.ccout)
    else:
      return False

  def extrapolarTodo(self):
    #code at this level indentation
    try:
      extras = {}
      if( self.bin2 !=' ' and self.bin2 != '' and self.bin2 != False):
        extras['similitud'] = self.simpleE()
        extras['bank'] = self.compleE()
        extras['advance'] = self.avanE()
      extras['xb1'] = self.grupE()
      extras['xb2'] = self.fivE()
      extras['xb3'] = self.xiiiiE()
      extras['xb4'] = self.xiiiE()
      extras['xb5'] = self.xiE()
      extras['xb6'] = self.xiiE()
      return extras
      
    except:
        return False

# a = '5047054122454316'
# b = '5047054142341193'
#

# ALL EXTRA METHODS
# result = Extrapola(a,b).extrapolarTodo()
#
# MAP RESULT V IS THE METHOD NAME AND K IS THE VALUE
# for v,k in result.items():
#   print(v,k)
#
# POO METHOD
# object = Extrapola()
# Extrapola.bin1 = '<bin1>'
# Extrapola.bin2 = '<bin1>'
# Extrapola.method() => wich returns the String result

#/////////////////////////////////////////////////////////////////////////////////////////////
#   TOOLS IS BASED IN
#   CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
#   Copyright (C) 2020  
#
#   DISCLAIMER: This file is for informational and educational purposes only. 
#   We are not responsible for any misuse applied to it. All responsibility falls on the user
#
#   ||================================================================================||
#   || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
#   ||================================================================================||
#
#   Adapted BY Lanniscaf ALL RIGHTS RESERVED
#////////////////////////////////////////////////////////////////////////////////////////////////
