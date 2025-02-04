queries = open("../query_desc.51-100.short.txt", 'r', encoding='iso-8859-1').read().split("\n")


def get_model_dict(filepath):
    okapi_idf = open(filepath).read().split("\n")
    okapi_dict = {}
    okapi_scores = list(map(lambda x: float(x.split()[4]), okapi_idf))
    max_okapi = max(okapi_scores)
    min_okapi= min(okapi_scores)

    for q in range(0, 25):
        query = queries[q]
        query_id = query.split()[0][0:-1]
        query_results = list(filter(lambda val: val.startswith(query_id), okapi_idf))
        # okapi_scores = list(map(lambda x: float(x.split()[4]), query_results))
        # max_okapi = max(okapi_scores)
        doc_score_dict = {}
        for val in query_results:
            doc_id = val.split()[2]
            score = float(val.split()[4])
            doc_score_dict[doc_id] = (score-min_okapi)/(max_okapi-min_okapi)
        okapi_dict[query_id] = doc_score_dict
    return okapi_dict

def write_output(queryno, dict):
    query_content=""
    rank = 1
    for k, v in dict.items():
        if rank > 1000:
            break
        op = str(queryno) + " Q0" + " " + str(k) + " " + str(rank) + " " + str(v) + " Exp";
        query_content += ("\n"+op)
        rank += 1
    return query_content


okapi_dict=get_model_dict("okapi-idf-output.txt")
bm25=get_model_dict("bm25-output.txt")
laplace=get_model_dict("laplace-output.txt")
es_builtin=get_model_dict("elastisearch-output.txt")
jelnik=get_model_dict("jelnik-output.txt")

models=[es_builtin,bm25,okapi_dict]
all_doc_ids=open("../cache/all_doc_ids.txt").read().split("\n")


file_content = "";
for query in queries:
    query_id = query.split()[0][0:-1]
    score_query_doc = {}
    for doc in all_doc_ids:
        retrieved_in=0
        sum_scores=0
        for model in models:
            if doc in model[query_id].keys():
                retrieved_in += 1
                sum_scores += model[query_id][doc]
        total_score=sum_scores*retrieved_in
        score_query_doc[doc]=total_score
    print("writing file")
    file_content += write_output(query_id,
                                 {k: v for k, v in
                                  sorted(score_query_doc.items(), key=lambda item: item[1], reverse=True)})

with open("meta-fusion-output.txt", 'w',
          encoding='iso-8859-1') as output_file:
    file_content = file_content.strip()
    output_file.write(file_content)