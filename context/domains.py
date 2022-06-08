# context, fname, train, test, id, label
from dataclasses import dataclass
from abc import *

import googlemaps
import pandas as pd


@dataclass
class Dataset:
    dname: str
    sname: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, dname): self._dname = dname

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass

# new_file, csv, xls, json
class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self, file)-> str:
        pass

    @abstractmethod
    def csv(self)-> object:
        pass

    @abstractmethod
    def xls(self)-> object:
        pass

    @abstractmethod
    def json(self)-> object:
        pass

# Reader
class Reader(ReaderBase):
    def new_file(self, file)-> str:
        return file.context + file.fname

    def csv(self, fname)-> object:
        return pd.read_csv(f'{self.new_file(fname)}.csv', encoding='utf-8', thousands='')

    def xls(self, fname, header, cols)-> object:
        return pd.read_excel(f'{self.new_file(fname)}.xls', header=header, usecols=cols)

    def json(self, fname)-> object:
        return pd.read_json(f'{self.new_file(fname)}.json', encoding='utf-8')

    def gmaps(self)-> object:
        return googlemaps.Client(key='')

# Printer
class Printer(PrinterBase):
    def dframe(self):
        pass
