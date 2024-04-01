import json
import requests
import traceback
import pandas as pd
from flask import make_response, jsonify, current_app, request, send_file
from flask_restful import Resource, reqparse
from flask_sieve import Validator

class CompareData(Resource):
    @classmethod
    def get(cls):
        return {'hello': 'world'}


    @classmethod
    def post(cls):
        try:
            rules = {
                'source': ['required'], 
                'compare': ['required'],
            }
            # messages = {
            #     'name.required': 'Yikes! The name is required',
            #     'name.alpha': 'Yikes! The name must be a string',
            # }
            
            validator = Validator(rules=rules, request=request)
            if validator.passes():
                # print(request.files['source'])
                # print(request.files['compare'])
                source_df = pd.read_excel(request.files['source'])
                compare_df = pd.read_excel(request.files['compare'])

                source_df['source'] = 'source_df'
                compare_df['source'] = 'compare_df'
                combined_df = pd.concat([source_df, compare_df], ignore_index=True)
                only_in_df2 = combined_df[combined_df['source'] == 'compare_df']
                only_in_df2.to_excel('my_data.xlsx', index=False)
                return send_file('../my_data.xlsx')
            response = {
                "message": "you are not valid."
            }
            return make_response(jsonify(response), 500)
        except Exception as err:
            current_app.logger.error(traceback.format_exc())
            response = {
                "status": "error",
                "status_code": 500,
                "message": "System Error",
                "data": {},
            }
            return make_response(jsonify(response), 500)