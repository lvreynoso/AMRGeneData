#!python

import sys

def getGenes(path):
  argAnnotGenes = ''
  with open(path, 'r') as f:
    geneLines = []
    for line in f:
      if line[0] == '>':
        geneData = line[1:]
        print(geneData)
        geneLines.append(geneData)
    argAnnotGenes = ''.join(geneLines)
  return argAnnotGenes


def writeFile(filtered):
  with open('arg_genes.txt', 'w') as o:
    o.write(filtered)
  return

if __name__ == '__main__':
  cleanText = ""
  if len(sys.argv) == 2:
    print("Reading source file.")
    cleanText = getGenes(sys.argv[1])
  writeFile(cleanText)
  print("Done.")