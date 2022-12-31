# coding:utf8

from PyQt5.QtWidgets import (
    QApplication, QTableView, QFileSystemModel,
    QStyledItemDelegate,
    QAbstractItemView
)
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex


class TableModel(QAbstractTableModel):

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 4

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return 4

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.DisplayRole:
            return str((index.column(), index.row()))
        else:
            return None

class HighlightingRowsTable(QTableView):
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.setModel(TableModel())
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def mouseMoveEvent(self, e) -> None:
        index = self.indexAt(e.pos())
        self.selectRow(index.row())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    model = TableModel()
    hrt = HighlightingRowsTable()
    hrt.setModel(model)
    hrt.show()
    app.exec_()


