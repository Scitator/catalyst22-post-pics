class ILogger:

    def log_artifact(self, tag: str, artifact: object, ...) -> None:
        """Logs artifact to the logger."""
        pass

    def log_image(self, tag: str, image: np.ndarray, ...) -> None:
        """Logs image to the logger."""
        pass

    def log_hparams(self, hparams: Dict, ...) -> None:
        """Logs hyperparameters to the logger."""
        pass
    
    def log_metrics(self, metrics: Dict[str, float], ...) -> None:
        """Logs metrics to the logger."""
        pass

    def flush_log(self) -> None:
        """Flushes the logger."""
        pass

    def close_log(self) -> None:
        """Closes the logger."""
        pass