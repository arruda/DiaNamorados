# -*- coding: utf-8 -*-

import simplejson as json
import bz2

def decodificar(entrada):    
    return bz2.decompress(eval(entrada))


def lerPerguntas():
    f = open("data.json","r")
    perguntas = json.load(f)
    f.close()
    return perguntas

def lerCodigo():
    f = open("pass.txt","r")
    senha = f.readline()
    senha.replace("\n","")
    f.close()
    return senha
    

def perguntar(perguntas):
    for pergunta, gabarito in perguntas.iteritems(): 
        resp=""
        while(resp!=gabarito):
            print "***********************************"
            resp = raw_input("Pergunta:"+pergunta+"\n")
            if resp!= gabarito:
                print "Resposta errada =P"
                print "Tente outra vez!"

            else:
                print "Aew! Acertou o/"
            print "***********************************"
    
    
    return decodificar(lerCodigo())

def main():      

    
    print "========================================================================="
    print "Para conseguir seu presente você deverá responder essa serie de perguntas"
    print "Cada acerto te leva para mais perto do resultado"
    print "(responda apenas em letras minusculas)"
    print "========================================================================="

    perguntas = lerPerguntas()

    resultado = perguntar(perguntas)
    final = """====================================================================
Sua Senha:
====================================================================
"""
    print final + resultado

      
