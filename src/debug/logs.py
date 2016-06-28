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
"""Create the dictionary for log functions for unmatched logs for debugging.

Functions:
  + get_regex_list: Get the regular expressions and function list.
"""
from __future__ import absolute_import
import debug.debug as debug


def get_regex_list():
    """Return the regular expressions and functions list for this module."""
    regex = []

    # Blacklist - Messages that we want to ignore.
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_scheduleJob:agent:\w+ job:\w+ " +
                  r"scheduled at priority \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ gathering events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ firing events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ " +
                  r"rescheduling events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ sleeping " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveDatabaseThread_loop:\w+ collecting garbage"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveDatabaseThread_loop:\w+ sleeping " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_updateAgentPriorities:agent:\w+ " +
                  r"priority set to \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_distributeTokens: \w+ agents at " +
                  r"priority \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapiThread_sleep: Sleep\(\d+ ms\)"])

    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_addEntryport:" +
                  r"NetioReceiver_Entryport reused"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioSender_addDestination:" +
                  r"NetioSender_Destination reused"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacadeReceiver_loop:\w+ disowning receive " +
                  r"resource"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacadeReceiver_loop:\w+ parsing message"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_receiveFast:\w+ received \d+ bytes"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_Shmem_receive_rEA:\w+ blocking on 0X\w+"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_Shmem_receive_rEA:\w+ woke up"])

    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipantPresentation_reserve_participant_" +
                  r"index_entryports:Domain \d+:Trying to reserve " +
                  r"participant index=\d+..."])
    regex.append([debug.on_ignored_message,
                  r"DISCPluginManager_onAfterLocalEndpointEnabled:at " +
                  r"\{\w+,\w+\}"])

    regex.append([debug.on_ignored_message,
                  r"PRESPsService_onWriterResendEvent:writer resend event: " +
                  r"\(([\w,]+)\)"])

    regex.append([debug.on_ignored_message, r"^send failed: $"])
    regex.append([debug.on_ignored_message, r"^\s*locator:\s*$"])
    regex.append([debug.on_ignored_message, r"^\s*transport: \d+$"])
    regex.append([debug.on_ignored_message, r"^\s*address: [\d:]+$"])
    regex.append([debug.on_ignored_message, r"^[\d:]+$"])
    regex.append([debug.on_ignored_message, r"^\s*port: \d+$"])
    regex.append([debug.on_ignored_message, r"^\s{6}encapsulation:$"])
    regex.append([debug.on_ignored_message, r"^\s{3}transport_priority: \d+$"])
    regex.append([debug.on_ignored_message, r'^\s{3}aliasList: ""$'])

    # The rest of unmatched message will be saved into a file to analyze them.
    regex.append([debug.on_unmatched_message, r"(.*)"])

    return regex