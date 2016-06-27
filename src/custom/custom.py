# Log Parser for RTI Connext.
#
#   Copyright 2016 Real-Time Innovations, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""Log parsing functions for custom logs.

Functions:
  + on_custom_log: Parse a log with a custom prefix.
"""
from __future__ import absolute_import
from logger import log_event


def on_custom_log(match, state):
    """Parse a log with a custom prefix."""
    log_event("[App] " + match[0], state)
