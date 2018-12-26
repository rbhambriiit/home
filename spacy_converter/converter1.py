import spacy, json
from spacy.gold import GoldCorpus, minibatch, biluo_tags_from_offsets, tags_to_entities


def docs_from_offsets(nlp, gold):
    """Create a sequence of Docs from a sequence of text, entity-offsets pairs."""
    docs = []
    for text, entities in gold:
        doc = nlp(text)
        
#         print('default')
#         for ent in doc.ents:
#             print(ent.text, ent.start_char, ent.end_char, ent.label_)
        
        entities = entities['entities']
        tags = biluo_tags_from_offsets(doc, entities)
        if entities:
            for start, end, label in entities:
                span = doc.char_span(start, end, label=label)
#                 ents = list(doc.ents)
                
                if span:
#                     print('span', span)
#                     print('list(doc.ents)', list(doc.ents))
#                     print('label', label)
#                     doc.ents =  ents + [span]
                    doc.ents =  [span]

        if doc.ents:  # remove to return documents without entities too
            docs.append((doc, tags))
    return docs


def docs_to_trees(docs):
    """Create spaCy JSON training data from a sequence of Docs."""
    doc_trees = []
    for d, doc_tuple in enumerate(docs):
        doc, tags = doc_tuple
        try:
            tags_to_entities(tags)
        except Exception as e:
            print('\n===========Exception:\n', e)
            print('Dropping {}'.format(d))
            print('DEBUG doc_tuple:', doc_tuple)
            continue
            
        if not tags:
            print('Dropping {}'.format(d))
            continue
            
        sentences = []
        for s in doc.sents:
            s_tokens = []
            for t in s:
                token_data = {
                    'id': t.i,
                    'orth': t.orth_,
                    'tag': t.tag_,
                    'head': t.head.i - t.i,
                    'dep': t.dep_,
                    'ner': tags[t.i],
                }
                s_tokens.append(token_data)
            sentences.append({'tokens': s_tokens})
            
        doc_trees.append({
            'id': d,
            'paragraphs': [
                {
                    'raw': doc.text,
                    'sentences': sentences,
                }
            ]
        })
    return doc_trees


def train_data_to_json(train_data, nlp, output_json='train.json'):
    """
    Create spaCy JSON training data from a sequence as list available in
    train_data format - standard to spaCy users!

    modified and motivated
    from https://support.prodi.gy/t/prodigy-annotations-to-spacy-train/243/11
    https://github.com/explosion/spaCy/issues/2515

    phase1 of prodigy_to_spacy : not required here.
    train data is already in that format and no need of prodigy database

    docs_from_offsets: used as-is.
    docs_to_trees: used as-is.

    save to output_json

    """

    offsets = train_data
    # print 'offsets:', offsets

    docs = docs_from_offsets(nlp, offsets)
    # print 'docs:', docs

    trees = docs_to_trees(docs)
    # print 'trees:', trees

    with open(output_json, 'wt') as f:
        json.dump(trees, f)
    print('successfully converted to json:',  output_json)

    return True


if __name__ == "__main__":
    nlp = spacy.load('en')

    train_data = [
    (u"Uber blew through $1 million a week", {'entities':[(0, 4, 'ORG')]}),
    (u"Android Pay expands to Canada", {'entities':[(0, 11, 'PRODUCT'), (23, 30, 'GPE')]}),
    (u"Spotify steps up Asia expansion", {'entities':[(0, 8, "ORG"), (17, 21, "LOC")]}),
    (u"Google Maps launches location sharing", {'entities':[(0, 11, "PRODUCT")]}),
    (u"Google rebrands its business apps", {'entities':[(0, 6, "ORG")]}),
    (u"look what i found on google! joy", {'entities':[(21, 27, "PRODUCT")]})
    ]

    
    # something here should fail. does not fail at all!
    overlap1 = (u"Uber blew through $1 million a week", {'entities':[(0, 4, 'ORG'), (0, 4, 'overlap1')]})
    train_data.append(overlap1)
    
    overlap2 = (u"Uber blew through $1 million a week", {'entities':[(0, 4, 'ORG'), (0, 9, 'overlap2')]})
    train_data.append(overlap2)
    
    overlap3 = (u"Uber blew through $1 million a week", {'entities':[(0, 9, 'overlap3'), (0, 4, 'ORG')]})
    train_data.append(overlap3)

    train_data_to_json(train_data, nlp)

