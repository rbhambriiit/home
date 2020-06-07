## processing case level data

input_file = '../data/NCBItrainset_corpus/tmp.txt'

f = open(input_file, "r")

input_str_lines = f.readlines()
# print('input_str_lines=', input_str_lines)

case_text = None
case_annotation = None

for ix, input_str_line in enumerate(input_str_lines):
    print('ix=', ix)
    print('input_str_line=', input_str_line)

    if ix == 0:
        # contain title
        assert '|t|' in input_str_line
        case_id, case_title = input_str_line.split('|t|')
        print('case_id', case_id)
        print('case_title', case_title)
        case_text = case_title

        continue

    elif ix == 1:
        # contain abstract
        assert '|a|' in input_str_line
        case_id, case_abstract = input_str_line.split('|a|')
        print('case_id', case_id)
        print('case_abstract', case_abstract)

        case_text += case_abstract
        continue

    # else annotation line found.
    case_id, start_ix, end_ix, annotation_text, annotation_tag, annotation_id = input_str_line.split('\t')
    # start_ix = int(start_ix)
    # print('start_ix=', start_ix, type(start_ix))
    # end_ix = int(end_ix)
    # print('end_ix=', end_ix)
    annotation_text2 = case_text[int(start_ix) : int(end_ix)    ]
    # print('annotation_text2=', annotation_text2)

    assert annotation_text2 == annotation_text

    # add ix such as 'T1'
    annotation_ix = 'T' + str(ix - 1)

    annotation = annotation_ix + '\t' + annotation_tag + '\t' + start_ix + '\t' + end_ix + '\t' + annotation_text2

    if case_annotation is None:
        case_annotation = annotation
    else:
        case_annotation += annotation
    case_annotation += '\n'
    # break

print('case_text=', case_text)
print('case_annotation=', case_annotation)

# need conversion to BRAT format: https://brat.nlplab.org/standoff.html
print('case_id=', case_id, type(case_id))

op_txt_file_name = '../data/processed/' + case_id + '.txt'
with open(op_txt_file_name, "w") as f:
    f.write(case_text)

op_ann_file_name = '../data/processed/' + case_id + '.ann'
with open(op_ann_file_name, "w") as f:
    f.write(case_annotation)
