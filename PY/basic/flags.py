# exercise absl.flags
# https://abseil.io/docs/python/guides/flags


# python flags.py debug --name Jerry --age 33 --job=running -nodebug
# non debug mode
# Hi Jerry,
# you are 33 years old.
# job: running


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