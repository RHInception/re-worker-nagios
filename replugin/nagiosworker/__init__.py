#!/usr/bin/env python
# Copyright (C) 2014 SEE AUTHORS FILE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Nagios worker.
"""


from reworker.worker import Worker


class NagiosWorkerError(Exception):
    """
    Base exception class for NagiosWorker errors.
    """
    pass


class NagiosWorker(Worker):
    """
    Worker which can interact with Nagios.
    """

    def process(self, channel, basic_deliver, properties, body, output):
        """
        Executes nagios commands.

        `Params Required`:

        """
        # Ack the original message
        self.ack(basic_deliver)
        corr_id = str(properties.correlation_id)
        # Notify we are starting
        self.send(
            properties.reply_to, corr_id, {'status': 'started'}, exchange='')

        try:
            pass
        except NagiosWorkerError, fwe:
            # If a NagiosWorkerError happens send a failure, notify and log
            # the info for review.
            self.app_logger.error('Failure: %s' % fwe)

            self.send(
                properties.reply_to,
                corr_id,
                {'status': 'failed'},
                exchange=''
            )
            output.error(str(fwe))


def main():  # pragma nocover
    from reworker.worker import runner
    runner(NagiosWorker)


if __name__ == '__main__':  # pragma nocover
    main()
