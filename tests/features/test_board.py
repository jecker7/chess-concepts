import chess
import features


def test_board_features():
    f = features.Board(chess.STARTING_FEN)
    assert f.features() == {
        "endgame_type": None,
        "fullmove_number": 1,
        "is_check": False,
        "material_advantage": 0,
        "material_count": 98,
        "our_bishop_pair": False,
        "our_bishops": 2,
        "our_knights": 2,
        "our_majors": 3,
        "our_material_count": 49,
        "our_minors": 4,
        "our_non_pawn_pieces": 8,
        "our_number_of_bishop_moves": 0,
        "our_number_of_captures": 0,
        "our_number_of_checks": 0,
        "our_number_of_knight_moves": 4,
        "our_number_of_moves": 20,
        "our_number_of_pawn_moves": 16,
        "our_number_of_queen_moves": 0,
        "our_number_of_rook_moves": 0,
        "our_pawns": 8,
        "our_piece_count": 16,
        "our_queens": 1,
        "our_rooks": 2,
        "phase": 0,
        "piece_count": 32,
        "position_openness": 2,
        "their_bishop_pair": False,
        "their_bishops": 2,
        "their_knights": 2,
        "their_majors": 3,
        "their_material_count": 49,
        "their_minors": 4,
        "their_non_pawn_pieces": 8,
        "their_number_of_bishop_moves": 0,
        "their_number_of_captures": 0,
        "their_number_of_checks": 0,
        "their_number_of_knight_moves": 4,
        "their_number_of_moves": 20,
        "their_number_of_pawn_moves": 16,
        "their_number_of_queen_moves": 0,
        "their_number_of_rook_moves": 0,
        "their_pawns": 8,
        "their_piece_count": 16,
        "their_queens": 1,
        "their_rooks": 2,
        "turn": True,
    }
