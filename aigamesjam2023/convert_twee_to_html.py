import html
import re
import sys

def twee_to_twine(twee_text):
    passages = re.findall(r':: (\w+)[\n]+(.*?)(?=:: |\Z)', twee_text, re.DOTALL)

    passage_data = []
    for idx, (title, content) in enumerate(passages, start=1):
        escaped_content = html.escape(content).replace("\n", "\n")
        passage_data.append(
            f'<tw-passagedata pid="{idx}" name="{title}" tags="" position="{idx*225},{idx*75}" size="100,100">{escaped_content}</tw-passagedata>'
        )

    passage_data_str = "\n".join(passage_data)
    twine_data = f'''<tw-storydata name="ChatGPT - Dragon Story - 2023.09.19" startnode="1" creator="Twine" creator-version="2.7.1" format="Harlowe" format-version="3.3.7" ifid="3f672f5c-cfdf-45bc-aec3-bc258889acad" options="" tags="" zoom="1" hidden><style role="stylesheet" id="twine-user-stylesheet" type="text/twine-css"></style><script role="script" id="twine-user-script" type="text/twine-javascript"></script>{passage_data_str}</tw-storydata>'''

    return twine_data


if __name__ == '__main__':
    target_file = sys.argv[1]

    with open(target_file, "r") as file_handler:
        lines = file_handler.readlines()

    twee_text = ""
    for line in lines:
        twee_text += line

    output = twee_to_twine(twee_text)
    print(output)
