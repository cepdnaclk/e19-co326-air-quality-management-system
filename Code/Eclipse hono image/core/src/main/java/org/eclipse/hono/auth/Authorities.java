/*******************************************************************************
 * Copyright (c) 2016, 2018 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0
 *
 * SPDX-License-Identifier: EPL-2.0
 *******************************************************************************/

package org.eclipse.hono.auth;

import java.util.Map;

import org.eclipse.hono.util.ResourceIdentifier;

/**
 * A collection of authorities granted on resources and/or operations.
 *
 */
public interface Authorities {

    /**
     * Checks if these authorities include claims allowing an intended activity on a resource.
     *
     * @param resourceId The resource.
     * @param intent The intended activity on the resource
     * @return {@code true} if the activity is allowed.
     */
    boolean isAuthorized(ResourceIdentifier resourceId, Activity intent);

    /**
     * Checks if these authorities include claims allowing execution of an operation of a resource.
     *
     * @param resourceId The resource.
     * @param operation The operation to execute.
     * @return {@code true} if execution is allowed.
     */
    boolean isAuthorized(ResourceIdentifier resourceId, String operation);

    /**
     * Gets the authorities as a map of claims.
     *
     * @return The claims.
     */
    Map<String, Object> asMap();
}
