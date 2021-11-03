r"""This is a lab inventory reservation record management tool.

The tool is not used to reserve a device in the lab inventory,
but to manage the reservation record information in the labdocs database.
It support list/add/del/auto-flush for the reservation records

Usage:
  ops/netops/lab/b2/lre/inventory/utils/resvmgr
    --action {list|reserve|release}
    --user <user>
    --device <device(s)>
    --start <start-date>
    --end <end-date>

Examples:
  resvmgr --action=list --dev=cx01.slq14,bb01.oak15 --end=2021-03-30

    to list the reservations of device cx01.sql14 and bb01.oak15 which
    the reservation period has overlap with (current-date, 2021-03-30)

  resvmgr --action=list --user=lre --start=2020-10-01 --end=2021-03-30

    to list the reservations which the user name contains lre and
    the reservation period has overlap with the given range (2020-10-01,
    2021-03-30)

  resvmgr --action=reserve --dev=cx01.slq14,bb01.oak15 --user=lre-team@
          --end=2021-03-30

    to set reservation information for device cx01.sql14 and bb01.oak15 in
    which the user is lre-team and the reservation period is from start
    to end. If start or end is not specified, it implies current date.
    in this example (current-date, 2021-03-30)
    So if neither start nor end is given, then the reservation is for 'today'.

  resvmgr --action=release --dev=cx01.slq14,bb01.oak15 --user=lre-team@
          --start=2021-5-10 --end=2022-03-30

    to clear the reservation information which match below conditions:
        (the device is cx01.sql14 or bb01.oak15) and
        (the user is exactly lre-team@) and
        (the reservation period has overlap with the given range start--end).
    If the condition of user/dev/date is not given, it implies to match all.
    e.g. if only the user if given, then all the user's reservation record will
    be cleared
    If only one date of start or end is not specified, the missing date implies
    current date.

"""



from absl import app
from absl import flags
import sys


FLAGS = flags.FLAGS

flags.DEFINE_string('name', None, 'Your name.')
flags.DEFINE_integer('age', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_list('friends', None, 'Your friends')
flags.DEFINE_enum('gender', None, ['male', 'female'], 'Your gender.')
flags.DEFINE_boolean('healthy', True, 'You are healthy.')


def main(argv):
    if not any([FLAGS.friends, FLAGS.age, FLAGS.name, FLAGS.healthy]):
        app.usage()
        sys.exit(-1)

    print(f'Hi {FLAGS.name}, ')
    if FLAGS.age:
        print(f'you are {FLAGS.age} years old.')
    if FLAGS.gender:
        print(f'Gender: {FLAGS.gender}')
    if FLAGS.friends:
        print(f'Your friends: {FLAGS.friends}')
    if FLAGS.healthy:
        print('You are healthy.')
    else:
        print('You are not healthy')



if __name__ == '__main__':
    app.run(main)
