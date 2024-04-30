
def load_maia_network(elo, lc0_path=None, models_dir_path=None, time_limit=None):
    from move_prediction.maia_chess_backend import load_model_config

    valid_elos = [str(el) for el in range(1100, 2000, 100)]
    assert str(elo) in valid_elos, f"Invalid elo value: {elo}, model does not exist. Valid elos are: {valid_elos}"

    lc0_path = f"lc0-exe-folder/lc0.exe" if lc0_path is None else lc0_path
    models_dir_path = f'move_prediction/model_files/{elo}' if models_dir_path is None else models_dir_path

    model, config = load_model_config(config_dir_path=models_dir_path, lc0Path=lc0_path)
    print('Model loaded successfully!')
    model.limits.time = time_limit if time_limit is not None else 1
    return model


if __name__ == '__main__':
    import chess
    model = load_maia_network(1200)
    topk = 10
    print(model.getTopMovesCP(chess.Board(), topk))

