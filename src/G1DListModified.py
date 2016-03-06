from pyevolve.GenomeBase import GenomeBase
from random import randint as rand_randint
from pyevolve import Consts, Util
import random

class G1DListModified(GenomeBase):

   evaluator = None
   initializator = None
   mutator = None
   crossover = None

   def __init__(self, size):
      """ The initializator of G1DListModified representation,
      size parameter must be specified """
      GenomeBase.__init__(self)
      self.genomeList = []
      self.listSize = size
      self.initializator.set(Consts.CDefG1DListInit)
      self.mutator.set(Consts.CDefG1DListMutator)
      self.crossover.set(Consts.CDefG1DListCrossover)

   def __eq__(self, other):
      """ Compares one chromosome with another """
      cond1 = (self.genomeList == other.genomeList)
      cond2 = (self.listSize   == other.listSize)
      return True if cond1 and cond2 else False

   def __mul__(self, other):
      """ Multiply every element of G1DListModified by "other" """
      newObj = self.clone()
      for i in xrange(len(newObj)):
         newObj[i] *= other
      return newObj

   def __add__(self, other):
      """ Plus every element of G1DListModified by "other" """
      newObj = self.clone()
      for i in xrange(len(newObj)):
         newObj[i] += other
      return newObj

   def __sub__(self, other):
      """ Plus every element of G1DListModified by "other" """
      newObj = self.clone()
      for i in xrange(len(newObj)):
         newObj[i] -= other
      return newObj

   def __getslice__(self, a, b):
      """ Return the sliced part of chromosome """
      return self.genomeList[a:b]

   def __getitem__(self, key):
      """ Return the specified gene of List """
      return self.genomeList[key]

   def __setitem__(self, key, value):
      """ Set the specified value for an gene of List """
      self.genomeList[key] = value

   def __iter__(self):
      """ Iterator support to the list """
      return iter(self.genomeList)
   
   def __len__(self):
      """ Return the size of the List """
      return len(self.genomeList)
      
   def __repr__(self):
      """ Return a string representation of Genome """
      ret = GenomeBase.__repr__(self)
      ret += "- G1DListModified\n"
      ret += "\tList size:\t %s\n" % (self.listSize,)
      ret += "\tList:\t\t %s\n\n" % (self.genomeList,) 
      return ret

   def append(self, value):
      self.genomeList.append(value)

   def clearList(self):
      """ Remove all genes from Genome """
      del self.genomeList[:]
   
   def copy(self, g):
      GenomeBase.copy(self, g)
      g.listSize = self.listSize
      g.genomeList = self.genomeList[:]
   
   def clone(self):
      newcopy = G1DListModified(self.listSize)
      self.copy(newcopy)
      return newcopy

   def getListSize(self):
      return self.listSize