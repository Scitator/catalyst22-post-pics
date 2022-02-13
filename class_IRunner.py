class IRunner:
    # hardware accelerator setup
    def get_engine(self) -> IEngine: pass

    # expriment components setup: the data, the model, etc
    def get_loaders(self) -> "OrderedDict[str, DataLoader]": pass
    def get_model(self) -> Model: pass
    def get_criterion(self) -> Optional[Criterion]: pass
    def get_optimizer(self, model: Model) -> Optional[Optimizer]: pass
    def get_scheduler(self, optimizer: Optimizer) -> Optional[Scheduler]: pass

    # monitoring systems setup
    def get_loggers(self) -> Dict[str, ILogger]: pass
    def log_artifact(self, *args, **kwargs) -> None: pass
    def log_image(self, *args, **kwargs) -> None: pass
    def log_hparams(self, *args, **kwargs) -> None: pass
    def log_metrics(self, *args, **kwargs) -> None: pass

    # extra logic setup: metrics and deep learning tricks
    def get_callbacks(self) -> "OrderedDict[str, Callback]": pass
    def _run_event(self, event: str) -> None:
        for callback in self.callbacks.values():
            getattr(callback, event)(self)

    def handle_batch(self, batch: Mapping[str, Any]) -> None:
        """Inner method to handle specified data batch."""
        pass

    def _run_loader(self) -> None:
        for self.batch in self.loader:
            self._run_event("on_batch_start")
            self.handle_batch(batch=self.batch)
            self._run_event("on_batch_end")

    def _run_epoch(self) -> None:
        for self.loader_key, self.loader in self.loaders.items():
            self._run_event("on_loader_start")
            self._run_loader()
            self._run_event("on_loader_end")

    def _run_experiment(self) -> None:
        self._run_event("on_epoch_start")
        self._run_epoch()
        self._run_event("on_epoch_end")

    def run(self) -> "IRunner":
        self._run_event("on_experiment_start")
        self._run_experiment()
        self._run_event("on_experiment_end")
        return self