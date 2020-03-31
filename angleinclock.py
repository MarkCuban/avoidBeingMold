import click

HOUR_PIECE = 30


hour = float(click.prompt('hour'))
minute = float(click.prompt('minute'))


if hour > 24:
    print('input a logical hour')
elif hour >= 12:
    hour -= 12

minute_hand = (minute/60)*360
hour_hand = (hour+(minute/60))*HOUR_PIECE

#print('hand is ', minute_hand, hour_hand)
print('angle is ', abs(minute_hand-hour_hand))






