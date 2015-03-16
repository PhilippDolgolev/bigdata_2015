# encoding: utf-8

    #�� ������� �������� ������ ������� �������� ����� �����, ��� ��� ��������� �� ���
    #�� ������ ��������� ���������, ���� ���� �������� ���������, ������� ���������, �� ��������� ��
    #����������� ����� ������:
    #���� ���������, �� ��������������, ���������� ����� ������� � value � �������� � ��� �����

from pregel import Vertex, Pregel
from hw04util import *
from random import randint
import sys

vertices = {}
num_workers = 1

def main(filename):
    global vertices
    # ������ ���� �� �����, ��������� ����������� TransVertex
    vertices = read_graph(filename, TransVertex)
    num_vertices = len(vertices)

    for v in vertices.values():
        v.value = set()

    # ��������� �������,
    # ���-�� ��������� == ����� ������ �������� ���� � ����� <= ���������� ������
    p = Pregel(vertices.values(), num_workers, num_vertices)
    p.run()

    # ��� ������ ������� � values ����� ������ ���� ������, ���������� �� ���
    print("Completed in %d supersteps" % p.superstep)

    trans_graph = {}
    for v in p.vertices:
        trans_graph[v.id] = []
    for vertice in p.vertices:
        for p in vertice.value:
            trans_graph[p].append(str(vertice.id))
    for vertice in trans_graph:
        if trans_graph[vertice]:
            print("{0} {1}".format(vertice, ",".join(trans_graph[vertice])))
        else:
            print("{0} ==".format(vertice))

class TransVertex(Vertex):
        def __init__(self, id):
            Vertex.__init__(self, id, None, [])
            self.value = set()          # ��-�� ��������� �������
            self.new_parents = set()    # ����� ������ ��������� ���������

        def update(self):
                global vertices

                if self.superstep == 0:
                    self.active = True
                    # �������� ���� �����, ��� ��� ����������� �� ������� �������
                    self.new_parents.add(self.id)
                else:
                    self.active = False
                    if self.incoming_messages:
                        # ��������� ���������� ����� �������
                        message_parents = set()
                        for (v, upd_parents) in self.incoming_messages:
                            message_parents.update(upd_parents)

                        # ������� ��� ��������� ������� �������
                        self.new_parents = message_parents.difference(self.value)
                        if self.new_parents:
                            # ������ ��������, �.�. ���������� ����� ����������� ������
                            self.active = True
                            self.value.update(self.new_parents)

                if self.active:
                    # �������� ������� ������ ���������� ���� ����� � ����� �������
                    self.outgoing_messages = [(vertex,self.new_parents) for vertex in self.out_vertices]


if __name__ == "__main__":
        main(sys.argv[1])