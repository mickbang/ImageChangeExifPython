import requests

# Define your cookies
cookies = {
    '__zlcmid': '1D7lP0YejLnD859',
    'TY_SESSION_ID': '2bffbc04-80c3-4317-945e-250caf389dee',
    '__zlcmid': '1D7lP0YejLnD859',
    'utc_offset': '-480',
    '__zlcmid': '1D7lP0YejLnD859',
}

headers = {
    'cookie':'__zlcmid=1D7lP0YejLnD859; TY_SESSION_ID=2bffbc04-80c3-4317-945e-250caf389dee; utc_offset=-480; change_histories_smart_listing_per_page=10; activities_smart_listing_per_page=10; _ezyform_session=3f7448a2bf128df1844b07d481c2f2f0; _gid=GA1.3.1474318419.1684385368; _ga=GA1.1.935238659.1659405895; _ga_JCG2462ZSK=GS1.1.1684484769.38.0.1684484769.60.0.0',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'referer':'https://staging.greendeal.com.au/admin/pvds?utf8=✓&q[no_model_fields][filter_company_title]=Company+Name&q[company_id_eq]=&q[company_id_eq]=&q[no_model_fields][contract_type_filter]=contract_code&q[price_contract_contract_code_cont]=&q[addon_management_contract_code_cont]=&q[company_account_manager_eq]=&q[last_operator_id_eq]=&q[agent_id_in][]=&q[reference_cont]=&q[gwtid_start]=&q[pvd_num_start]=&q[price_eq]=&tags=&q[status_eq]=Installed&q[recreated_eq]=&q[gst_eq]=&q[flag_eq]=&q[compliant_eq]=&q[require_check_eq]=&q[created_via_eq]=&q[payment_status_eq]=&q[trade_mode_eq]=&q[ps_flag_eq]=&q[pvd_system_connected_eq]=&q[resolution_eq]=&q[spv_check_eq]=&q[pending_sold_eq]=&q[pvd_installer_installer_id_eq]=&q[pvd_install_address_state_eq]=&q[pvd_installer_installer_blacklist_eq]=&q[no_model_fields][quick_panel_model]=&q[no_model_fields][quick_inverter_model]=&q[surrendered_eq]=&q[customer_po_cont]=&q[xero_sync_eq]=&q[stc_check_err_eq]=&q[pvd_install_address_uncertain_flg_eq]=&q[no_model_date_filters][0][date_title]=approve_date&q[no_model_date_filters][0][begin_date]=&q[no_model_date_filters][0][end_date]=&q[no_model_date_filters][0][_destroy]=false&current_status=search&commit=Search'
}

# Send a GET request to the target URL with cookies
response = requests.get("https://staging.greendeal.com.au/admin/pvds/258304", headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract data from the response
    data = response.text

    # Process the extracted data as needed
    processed_data = data.strip()

    # Output the processed data
    print(processed_data)
