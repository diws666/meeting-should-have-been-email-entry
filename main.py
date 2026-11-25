import os

LINE = "We held a meeting about the meeting. The meeting about the meeting has now been scheduled for next week."  # verified: 104 characters

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
