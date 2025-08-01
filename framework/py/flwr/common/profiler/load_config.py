# Copyright 2025 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Configuration loader."""

import tomli


class LoadConfig:
    """Configurtion loader class."""

    def __init__(self, config_file) -> None:
        """Initialize the constructor."""
        with open(config_file, "rb") as f:
            self.config = tomli.load(f)

    def get_fl_config(self) -> dict[str, any]:
        """Getting the federated learning config."""
        root = self.config["tool"]["flwr"]["app"]["config"]
        return {
            "num_server_rounds": root["num-server-rounds"],
            "fraction_fit": root["fraction-fit"],
            "fraction_evaluate": root["fraction-evaluate"],
            "local_epochs": root["local-epochs"],
            "server_device": root["server-device"],
            "use_wandb": root["use-wandb"],
            "min_fit_clients": root["min-fit-clients"],
            "min_evaluate_clients": root["min-evaluate-clients"],
            "min_available_clients": root["min-available-clients"],
            "num_clients": root["number-clients"],
            "learning_rate": root["learning-rate"],
        }

    def get_he_config(self) -> dict[str, any]:
        """Getting the homomorphic encryption config."""
        root = self.config["tool"]["federated_learning"]["he"]
        return {
            "enable": root["enable"],
            "context": {
                "client": root["context"]["path"]["client"],
                "server": root["context"]["path"]["server"],
            },
            "key": {
                "client": root["key"]["path"]["client"],
                "server": root["key"]["path"]["server"],
                "server_crypted": root["key"]["path"]["server-crypted"],
            },
            "library": root["library"],
            "schema": root["schema"],
            "poly_modulus_degree": root["poly-modulus-degree"],
            "coef_mod_bit": root["coeff-mod-bit-sizes"],
            "global_scale": root["global-scale"],
        }

    def get_nn_config(self) -> dict[str, any]:
        """Getting the nural config."""
        root = self.config["tool"]["federated_learning"]["nn"]
        return {
            "store_model": root["store-model"],
            "seed": root["seed"],
            "max_epochs": root["max-epochs"],
            "batch_size": root["batch-size"],
            "learning_rate": root["learning-rate"],
            "shuffle_buffer": root["shuffle-buffer"],
            "prefetch_buffer": root["prefetch-buffer"],
            "model_path": root["storage-model-path"],
            "model_save": root["model-save"],
            "checkpoint": root["checkpoint-save"],
            "input_shape": root["input-shape"],
            "num_classes": root["num-classes"],
            "model": root["model"],
            "verbose": root["verbose"],
            "shuffle": root["shuffle"],
            "validation_split": root["validation-split"],
        }

    def get_test_config(self) -> dict[str, any]:
        """Getting the test config."""
        root = self.config["tool"]["federated_learning"]["test"]["dataset"]
        return {
            "dataset": root["dataset"],
            "splitter": root["splitter"],
            "num_clients": root["num-clients"],
            "num_workers": root["num-workers"],
            "batch_size": root["batch-size"],
            "resize": root["resize"],
            "seed": root["seed"],
            "data_path": root["data-path"],
            "validation_data": root["validation-data"],
            "classes": root["classes"],
            "normalization": {
                "mean": root["normalization"]["mean"],
                "std": root["normalization"]["std"],
            },
        }

    def get_stats_config(self) -> dict[str, any]:
        """Getting the stats config."""
        root = self.config["tool"]["federated_learning"]["stats"]
        return {
            "enable": root["enable"],
            "plots": root["path"]["plots"],
            "reports": root["path"]["reports"],
        }

    def get_quantum_config(self) -> dict[str, any]:
        """Getting the quantum config."""
        root = self.config["tool"]["federated_learning"]["quantum"]
        return {
            "enable": root["enable"],
            "num_qubits": root["num-qubits"],
            "num_layers": root["num-layers"],
        }

    def get_network_config(self) -> dict[str, any]:
        """Getting the network config."""
        root = self.config["tool"]["federated_learning"]["simulation"]["network"]
        return {
            "enable": root["enable"],
            "technology": root["technology"],
            "protocol": root["protocol"],
            "bandwidth": root["bandwidth"],
            "latency": root["latency"],
            "packet_loss": root["packet-loss"],
            "jitter": root["jitter"],
            "address": root["server"]["address"],
            "port": root["server"]["port"],
        }
