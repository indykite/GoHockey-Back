/*
 * GoGretzky API
 * Go Gretzky is committed to offering you an outstanding range of world class hockey products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.InlineResponse200;
import org.openapitools.client.model.InlineResponse2001;
import org.openapitools.client.model.UserAddressBody;
import org.openapitools.client.model.UserChildBody;
import org.openapitools.client.model.UserSubscriptionBody;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Ignore
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    
    /**
     * Welcome to the GoGretzky API
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void rootGetTest() throws ApiException {
        String response = api.rootGet();

        // TODO: test validations
    }
    
    /**
     * Get the home address of the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userAddressGetTest() throws ApiException {
        InlineResponse200 response = api.userAddressGet();

        // TODO: test validations
    }
    
    /**
     * Add a home address to the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userAddressPostTest() throws ApiException {
        UserAddressBody userAddressBody = null;
        api.userAddressPost(userAddressBody);

        // TODO: test validations
    }
    
    /**
     * Get the child by id
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userChildChildIdGetTest() throws ApiException {
        String childId = null;
        UserChildBody response = api.userChildChildIdGet(childId);

        // TODO: test validations
    }
    
    /**
     * Add a child to the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userChildPostTest() throws ApiException {
        UserChildBody userChildBody = null;
        api.userChildPost(userChildBody);

        // TODO: test validations
    }
    
    /**
     * Get the email of the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userEmailGetTest() throws ApiException {
        String response = api.userEmailGet();

        // TODO: test validations
    }
    
    /**
     * Get the subscription of the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userSubscriptionGetTest() throws ApiException {
        InlineResponse2001 response = api.userSubscriptionGet();

        // TODO: test validations
    }
    
    /**
     * Add a subscription to the logged in user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userSubscriptionPostTest() throws ApiException {
        UserSubscriptionBody userSubscriptionBody = null;
        api.userSubscriptionPost(userSubscriptionBody);

        // TODO: test validations
    }
    
}
