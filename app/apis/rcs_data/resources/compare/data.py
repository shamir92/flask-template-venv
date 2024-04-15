import json
import requests
import traceback
import pandas as pd
import hashlib
from flask import make_response, jsonify, current_app, request, send_file
from flask_restful import Resource, reqparse
from flask_sieve import Validator

class CompareData(Resource):
    
    @classmethod
    def hash_row(cls,row):
        """Generate a hash for each row."""
        row_string = ''.join(map(str, row))
        return hashlib.sha256(row_string.encode()).hexdigest()
    @classmethod
    def hash_multiple_columns(cls,row, columns):
        """Generate a hash from multiple column values in a row."""
        # Create a string by concatenating the values of specified columns
        combined_string = ''.join(str(row[col]) for col in columns)
        return hashlib.sha256(combined_string.encode()).hexdigest()

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
                source_df = pd.read_excel(request.files['source'])
                compare_df = pd.read_excel(request.files['compare'])
                columns_to_hash = ['concat_update_judul', 'concat_update_tipe_kewajiban', 'concat_update_sanksi', 'concat_update_checklist', 'concat_update_peraturan_kewajiban', 'concat_update_peraturan_sanksi']

                ## Cleaning the data type of needed column for each dataframe 
                source_df['Topik'] = source_df['Topik'].astype(str).str.strip()
                del source_df['Kewajiban']
                del source_df['Notes']
                del source_df['Tipe Kewajiban']
                del source_df['Sanksi'] 
                del source_df['Checklist']
                del source_df['peraturan_kewajiban']
                del source_df['peraturan_sanksi']
                del source_df['Tag']
                del source_df['kewajiban_uuid']
                del source_df['Latest Publish']
                del source_df['Update status']
                del source_df['Update Notes']

                # source_df['Update status'] = source_df['Update status'].astype(str)
                source_df['Update Judul'] = source_df['Update Judul'].astype(str).str.strip()
                # source_df['concat_update_judul'] = source_df['Update Judul'].str.lower()
                # source_df['concat_update_judul'] = source_df['concat_update_judul'].str.replace(r'\s+', '', regex=True)

                # source_df['Update Notes'] = source_df['Update Notes'].astype(str)
                source_df['Update Tipe Kewajiban'] = source_df['Update Tipe Kewajiban'].astype(str).str.strip()
                # source_df['concat_update_tipe_kewajiban'] = source_df['Update Tipe Kewajiban'].str.lower()
                # source_df['concat_update_tipe_kewajiban'] = source_df['concat_update_tipe_kewajiban'].str.replace(r'\s+', '', regex=True)
                
                source_df['Update Sanksi'] = source_df['Update Sanksi'].astype(str).str.strip()
                # source_df['concat_update_sanksi'] = source_df['Update Sanksi'].str.lower()
                # source_df['concat_update_sanksi'] = source_df['concat_update_sanksi'].str.replace(r'\s+', '', regex=True)

                source_df['Update Checklist'] = source_df['Update Checklist'].astype(str).str.strip()
                # source_df['concat_update_checklist'] = source_df['Update Checklist'].str.lower()
                # source_df['concat_update_checklist'] = source_df['concat_update_checklist'].str.replace(r'\s+', '', regex=True)

                source_df['Update peraturan_kewajiban'] = source_df['Update peraturan_kewajiban'].astype(str).str.strip()
                # source_df['concat_update_peraturan_kewajiban'] = source_df['Update peraturan_kewajiban'].str.lower()
                # source_df['concat_update_peraturan_kewajiban'] = source_df['concat_update_peraturan_kewajiban'].str.replace(r'\s+', '', regex=True)

                source_df['Update peraturan_sanksi'] = source_df['Update peraturan_sanksi'].astype(str).str.strip()
                # source_df['concat_update_peraturan_sanksi'] = source_df['Update peraturan_sanksi'].str.lower()
                # source_df['concat_update_peraturan_sanksi'] = source_df['concat_update_peraturan_sanksi'].str.replace(r'\s+', '', regex=True)

                source_df['hash'] = source_df.apply(cls.hash_row, axis=1)
                # source_df['hash'] = source_df.apply(lambda row: cls.hash_multiple_columns(row, columns_to_hash), axis=1)
                # source_df['Tag'] = source_df['Tag'].astype(str)
                # source_df['source'] = source_df['source'].astype(str)

                compare_df['Topik'] = compare_df['Topik'].astype(str).str.strip()
                # compare_df['Kewajiban'] = compare_df['Kewajiban'].astype(str)
                # compare_df['Notes'] = compare_df['Notes'].astype(str)
                # compare_df['Tipe Kewajiban'] = compare_df['Tipe Kewajiban'].astype(str)
                # compare_df['Sanksi'] = compare_df['Sanksi'].astype(str)
                # compare_df['Checklist'] = compare_df['Checklist'].astype(str)
                # compare_df['peraturan_kewajiban'] = compare_df['peraturan_kewajiban'].astype(str)
                # compare_df['peraturan_sanksi'] = compare_df['peraturan_sanksi'].astype(str)

                del compare_df['Kewajiban'] 
                del compare_df['Notes'] 
                del compare_df['Tipe Kewajiban'] 
                del compare_df['Sanksi'] 
                del compare_df['Checklist'] 
                del compare_df['peraturan_kewajiban'] 
                del compare_df['peraturan_sanksi']
                del compare_df['Tag']
                del compare_df['kewajiban_uuid']     
                del compare_df['Latest Publish']
                del compare_df['Update status']
                del compare_df['Update Notes']

                # # compare_df['Update status'] = compare_df['Update status'].astype(str)
                # compare_df['Update Judul'] = compare_df['Update Judul'].astype(str)
                # # compare_df['Update Notes'] = compare_df['Update Notes'].astype(str)
                # compare_df['Update Tipe Kewajiban'] = compare_df['Update Tipe Kewajiban'].astype(str)
                # compare_df['Update Sanksi'] = compare_df['Update Sanksi'].astype(str)
                # compare_df['Update Checklist'] = compare_df['Update Checklist'].astype(str)
                # compare_df['Update peraturan_kewajiban'] = compare_df['Update peraturan_kewajiban'].astype(str)
                # compare_df['Update peraturan_sanksi'] = compare_df['Update peraturan_sanksi'].astype(str)
                # compare_df['hash'] = compare_df.apply(cls.hash_row, axis=1)

                # source_df['Update status'] = source_df['Update status'].astype(str)
                compare_df['Update Judul'] = compare_df['Update Judul'].astype(str).str.strip()
                # compare_df['concat_update_judul'] = compare_df['Update Judul'].str.lower()
                # compare_df['concat_update_judul'] = compare_df['concat_update_judul'].str.replace(r'\s+', '', regex=True)

                # source_df['Update Notes'] = source_df['Update Notes'].astype(str)
                compare_df['Update Tipe Kewajiban'] = compare_df['Update Tipe Kewajiban'].astype(str).str.strip()
                # compare_df['concat_update_tipe_kewajiban'] = compare_df['Update Tipe Kewajiban'].str.lower()
                # compare_df['concat_update_tipe_kewajiban'] = compare_df['concat_update_tipe_kewajiban'].str.replace(r'\s+', '', regex=True)
                
                compare_df['Update Sanksi'] = compare_df['Update Sanksi'].astype(str).str.strip()
                # compare_df['concat_update_sanksi'] = compare_df['Update Sanksi'].str.lower()
                # compare_df['concat_update_sanksi'] = compare_df['concat_update_sanksi'].str.replace(r'\s+', '', regex=True)

                compare_df['Update Checklist'] = compare_df['Update Checklist'].astype(str).str.strip()
                # compare_df['concat_update_checklist'] = compare_df['Update Checklist'].str.lower()
                # compare_df['concat_update_checklist'] = compare_df['concat_update_checklist'].str.replace(r'\s+', '', regex=True)

                compare_df['Update peraturan_kewajiban'] = compare_df['Update peraturan_kewajiban'].astype(str).str.strip()
                # compare_df['concat_update_peraturan_kewajiban'] = compare_df['Update peraturan_kewajiban'].str.lower()
                # compare_df['concat_update_peraturan_kewajiban'] = compare_df['concat_update_peraturan_kewajiban'].str.replace(r'\s+', '', regex=True)

                compare_df['Update peraturan_sanksi'] = compare_df['Update peraturan_sanksi'].astype(str).str.strip()
                # compare_df['concat_update_peraturan_sanksi'] = compare_df['Update peraturan_sanksi'].str.lower()
                # compare_df['concat_update_peraturan_sanksi'] = compare_df['concat_update_peraturan_sanksi'].str.replace(r'\s+', '', regex=True)

                compare_df['hash'] = compare_df.apply(cls.hash_row, axis=1)
                # compare_df['hash'] = compare_df.apply(lambda row: cls.hash_multiple_columns(row, columns_to_hash), axis=1)


                compare_df_non_matching = compare_df[~compare_df['hash'].isin(source_df['hash'])]
                # del compare_df_non_matching['concat_update_peraturan_sanksi']
                # del compare_df_non_matching['concat_update_peraturan_kewajiban']
                # del compare_df_non_matching['concat_update_checklist']
                # del compare_df_non_matching['concat_update_sanksi'] 
                # del compare_df_non_matching['concat_update_tipe_kewajiban']
                # del compare_df_non_matching['concat_update_judul'] 
                print(compare_df_non_matching)
                compare_df_non_matching.to_excel('my_data.xlsx')
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