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
"""Profiler."""

import threading
import time

import psutil


class Profiler:
    """Profiler class."""

    def __init__(self) -> None:
        """Initialize a constructor profiler."""
        self.events: list[any] = []

    def start(self) -> None:
        """Start profiling."""
        raise NotImplementedError()

    def stop(self) -> None:
        """Stop profiling."""
        raise NotImplementedError()

    def __enter__(self):
        """Enter to profiling."""
        self.start()
        return self

    def __exit__(self, cls, exc, tb) -> None:
        """Stop profiling."""
        self.stop()


class TimeProfiler(Profiler):
    """Time profiler class."""

    def start(self) -> None:
        """Start profiling."""
        self._start_time = time.perf_counter()

    def stop(self) -> None:
        """Stop profiling."""
        end_time = time.perf_counter()
        delta_time = end_time - self._start_time
        self.events.append(delta_time)


class MemoryProfiler(Profiler):
    """Memory profiler class."""

    def __init__(self) -> None:
        """Initialize a constructor profiler."""
        super().__init__()
        self._tracking = False
        self._process = psutil.Process()

    def _tracer(self) -> None:
        """Tracer."""
        while self._tracking:
            self._peek_memory = max(self._peek_memory, self._process.memory_info().vms)

    def start(self) -> None:
        """Start profiling."""
        self._thread = threading.Thread(target=self._tracer, daemon=True)

        self._tracking = True
        self._peek_memory = 0
        self._thread.start()
        while not self._peek_memory:
            pass
        self._base_memory = self._peek_memory

    def stop(self) -> None:
        """Stop profiling."""
        self._tracking = False
        self._thread.join()
        del self._thread

        delta_memory = self._peek_memory - self._base_memory
        self.events.append(delta_memory)
