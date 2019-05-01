import csv
import json

csvfile = open('oregonstateuniversity.csv', 'r')
jsonfile = open('oregonstateuniversity.json', 'w')

fieldnames = ("edge_liked_by.count","edge_media_to_caption.edges","edge_media_to_comment.count","id", "owner.id", "tags", "taken_at_timestamp")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)