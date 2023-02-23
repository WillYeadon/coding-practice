# NxN Jigsaw puzzle.

# unique piece id and edges
class Piece:
    def __init__(self, piece_id, edges):
        self.piece_id = piece_id
        self.edges = edges
        
# unique edge id and colours which can be used to identify
# a match. Also bool as to whether connected
class Edge:
    def __init__(self, edge_id, colors):
        self.edge_id = edge_id
        self.colors = colors
        self.connected = False

def find_corner_piece(piece):
    pass

def find_matching_piece(pieces):
    pass


def solve_puzzle(pieces):
    puzzle = [[None for _ in range(len(pieces))] for _ in range(len(pieces))]
    # Randomly selects corner piece
    corner_piece = find_corner_piece(pieces)
    # Rotates until edge found
    corner_piece.rotate_flat_edge()
    # Places corner at [0][0]
    puzzle[0][0] = corner_piece
    for row in range(len(pieces)):
        for col in range(len(pieces)):
            if puzzle[row][col] is None:
                # Hypothetical functions to get matches in place
                if col == 0:
                    matching_edge = puzzle[row-1][col].get_bottom_edge()
                else:
                    matching_edge = puzzle[row][col-1].get_right_edge()
                piece = find_matching_piece(pieces, matching_edge)
                piece.rotate_to_match(matching_edge)
                puzzle[row][col] = piece
    return puzzle